from Tuleap.RestClient.Projects import Projects
from lib.base import BaseTuleapAction


class CreateProject(BaseTuleapAction):
    def run(self, short_name, description, label):
        success = self._login()
        if success:
            # Projects
            projects = Projects(self.connection)
            success = projects.create_project(short_name, description, label)
            if success:
                self.response = projects.get_data()

                return True, self.response

        return False, self.response
