from git import Repo

import enum
from internal.exceptions import InvalidFormat

class CommitMessageFormat(enum.Enum):
    CONVENTIONAL = "conv"
    CONVENTIONAL_EMOJI = "conv-emoji"

class CLI:
    def install(self, location: str = ".", format: CommitMessageFormat = CommitMessageFormat.CONVENTIONAL) -> None:
        """Installs Git alias for the repository of the given location"""

        commitMessageFormat = ""
        try:
            commitMessageFormat = CommitMessageFormat(format)
        except ValueError:
            raise InvalidFormat
        if commitMessageFormat == CommitMessageFormat.CONVENTIONAL:
            pass
        elif commitMessageFormat == CommitMessageFormat.CONVENTIONAL_EMOJI:
            pass

    def generate_commit_message(self, location: str = ".") -> str:
        """
        Generates commit message with the help
        of the given location of the repository    
        """
        repo = Repo(location)
        return repo.git.status()
        pass