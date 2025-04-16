import os
from datetime import datetime

class FSLog:
    @staticmethod
    def get_current_timestamp():
        return datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')

    def __init__(self, log_folder_path="Logs", max_logs=10):
        self.log_folder_path = log_folder_path
        self.max_logs = max_logs+1
        self.colors = Colors()
        self.DEBUG_STATUS = False
        os.makedirs(self.log_folder_path, exist_ok=True)
        self.log_file_name = os.path.join(
            self.log_folder_path,
            datetime.now().strftime("[%Y.%m.%d] [%H-%M-%S] Logs.txt")
        )
        with open(self.log_file_name, "a", encoding="utf-8"):
            pass
        self.manage_log_files()

    def usage_debug(self, func_name):
        if self.DEBUG_STATUS:
            message = f"Calling function: \"{func_name}\""
            log_entry = f"{self.get_current_timestamp()} [DEBUG] {message}"
            print(self.colors.colorize(log_entry, Colors.CYAN))
            self.write_to_file(log_entry)

    def server(self, message: str, color: tuple = None):
        self.usage_debug("server")
        return self.log(message, "SERVER", color)

    def logging(self, message: str, color: tuple = None):
        self.usage_debug("logging")
        return self.log(message, "LOGGING", color)

    def error(self, message: str, color: tuple = None):
        self.usage_debug("error")
        return self.log(message, "ERROR", color or Colors.RED)

    def warning(self, message: str, color: tuple = None):
        self.usage_debug("warning")
        return self.log(message, "WARNING", color or Colors.YELLOW)

    def info(self, message: str, color: tuple = None):
        self.usage_debug("info")
        return self.log(message, "INFO", color or Colors.BLUE)

    def debug(self, message: str, color: tuple = None):
        self.usage_debug("debug")
        return self.log(message, "DEBUG", color or Colors.CYAN)

    def custom(self, message: str, prefix: str, color: tuple = None):
        self.usage_debug("custom")
        return self.log(message, prefix, color)

    def log(self, message: str, prefix: str, color: tuple = None):
        log_entry = f"{self.get_current_timestamp()} [{prefix}] {message}"
        if color:
            print(self.colors.colorize(log_entry, color))
        else:
            print(log_entry)
        self.write_to_file(log_entry)
        return log_entry

    def write_to_file(self, content: str):
        with open(self.log_file_name, "a", encoding="utf-8") as log_file:
            log_file.write(content + "\n")

    def manage_log_files(self):
        self.usage_debug("manage_log_files")
        log_files = [
            os.path.join(self.log_folder_path, file)
            for file in os.listdir(self.log_folder_path)
            if os.path.isfile(os.path.join(self.log_folder_path, file))
        ]
        log_files.sort(key=os.path.getctime)
        while len(log_files) > self.max_logs-1:
            oldest_file = log_files.pop(0)
            try:
                os.remove(oldest_file)
            except Exception as e:
                self.error(f"Failed to remove old log file {oldest_file}: {e}")

    def lib_debug(self, toggle):
        self.usage_debug("lib_debug")
        if toggle.lower() not in ["on", "off"]:
            self.debug("Unexpected status")
        elif toggle.lower() == "on":
            self.DEBUG_STATUS = True
            self.debug(f"Debug toggled to \"{toggle.upper()}\"")
        else:
            self.DEBUG_STATUS = False
            self.debug(f"Debug toggled to \"{toggle.upper()}\"")

    def logging_stats(self, color: tuple = None):
        self.usage_debug("logging_stats")
        log_files = [
            os.path.join(self.log_folder_path, file)
            for file in os.listdir(self.log_folder_path)
            if os.path.isfile(os.path.join(self.log_folder_path, file))
        ]
        stats = (
            f"Current log-file: \"{os.path.basename(self.log_file_name)}\", "
            f"Total logs: {len(log_files)}/{self.max_logs-1}"
        )
        if log_files:
            current_size = os.path.getsize(self.log_file_name) / 1024  # KB
            stats += f", Size: {current_size:.2f} KB"
            last_modified = datetime.fromtimestamp(os.path.getmtime(self.log_file_name))
            stats += f", Modified: {last_modified.strftime('%Y-%m-%d %H:%M')}"
        return self.log(stats, "STATUS", color)

def create_logger(log_folder_path="Logs", max_logs=10):
    return FSLog(log_folder_path, max_logs)

class Colors:
    @staticmethod
    def colorize(text: str, rgb: tuple) -> str:
        r, g, b = rgb
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))
        return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)