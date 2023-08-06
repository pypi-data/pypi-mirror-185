from cli_ui import fatal

from gitlabform import EXIT_INVALID_INPUT
from gitlabform.configuration.core import KeyNotFoundException
from gitlabform.configuration.projects_and_groups import ConfigurationProjectsAndGroups


class ConfigurationCaseInsensitiveProjectsAndGroups(ConfigurationProjectsAndGroups):
    def __init__(self, config_path=None, config_string=None):
        super().__init__(config_path, config_string)
        self.find_almost_duplicates()

    def get_group_config(self, group) -> dict:
        """
        :param group: group/subgroup
        :return: configuration for this group/subgroup or empty dict if not defined,
                 ignoring the case
        """
        try:
            return self.get_case_insensitively(
                self.get("projects_and_groups"), f"{group}/*"
            )
        except KeyNotFoundException:
            return {}

    def get_project_config(self, group_and_project) -> dict:
        """
        :param group_and_project: 'group/project'
        :return: configuration for this project or empty dict if not defined,
                 ignoring the case
        """
        try:
            return self.get_case_insensitively(
                self.get("projects_and_groups"), group_and_project
            )
        except KeyNotFoundException:
            return {}

    def is_project_skipped(self, project) -> bool:
        """
        :return: if project is defined in the key with projects to skip,
                 ignoring the case
        """
        return self.is_skipped_case_insensitively(
            self.get("skip_projects", []), project
        )

    def is_group_skipped(self, group):
        """
        :return: if group is defined in the key with groups to skip,
                 ignoring the case
        """
        return self.is_skipped_case_insensitively(self.get("skip_groups", []), group)

    @staticmethod
    def get_case_insensitively(a_dict: dict, a_key: str):
        for dict_key in a_dict.keys():
            if dict_key.lower() == a_key.lower():
                return a_dict[dict_key]
        raise KeyNotFoundException()

    @staticmethod
    def is_skipped_case_insensitively(an_array: list, item: str) -> bool:
        """
        :return: if item is defined in the list to be skipped
        """
        item = item.lower()

        for list_element in an_array:
            list_element = list_element.lower()

            if list_element == item:
                return True

            if (
                list_element.endswith("/*")
                and item.startswith(list_element[:-2])
                and len(item) >= len(list_element[:-2])
            ):
                return True

        return False

    def find_almost_duplicates(self):

        # in GitLab groups and projects names are de facto case insensitive:
        # you can change the case of both name and path BUT you cannot create
        # 2 groups which names differ only with case and the same thing for
        # projects. therefore we cannot allow such entries in the config,
        # as they would be ambiguous.

        for path in [
            "projects_and_groups",
            "skip_groups",
            "skip_projects",
        ]:
            if self.get(path, 0):
                almost_duplicates = self._find_almost_duplicates(path)
                if almost_duplicates:
                    fatal(
                        f"There are almost duplicates in the keys of {path} - they differ only in case.\n"
                        f"They are: {', '.join(almost_duplicates)}\n"
                        f"This is not allowed as we ignore the case for group and project names.",
                        exit_code=EXIT_INVALID_INPUT,
                    )

    def _find_almost_duplicates(self, configuration_path):
        """
        Checks given configuration key and reads its keys - if it is a dict - or elements - if it is a list.
        Looks for items that are almost the same - they differ only in the case.
        :param configuration_path: configuration path, f.e. "group_settings"
        :return: list of items that have almost duplicates,
                 or an empty list if none are found
        """

        dict_or_list = self.get(configuration_path)
        if isinstance(dict_or_list, dict):
            items = dict_or_list.keys()
        else:
            items = dict_or_list

        items_with_lowercase_names = [x.lower() for x in items]

        # casting these to sets will deduplicate the one with lowercase names
        # lowering its cardinality if there were elements in it
        # that before lowering differed only in case
        if len(set(items)) != len(set(items_with_lowercase_names)):

            # we have some almost duplicates, let's find them
            almost_duplicates = []
            for first_item in items:
                occurrences = 0
                for second_item in items_with_lowercase_names:
                    if first_item.lower() == second_item.lower():
                        occurrences += 1
                        if occurrences == 2:
                            almost_duplicates.append(first_item)
                            break
            return almost_duplicates

        else:
            return []
