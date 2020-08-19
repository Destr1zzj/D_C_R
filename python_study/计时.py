import time
class Mytimer:
    def start(self):
        self.tms = time.localtime()
        print("start!")
    def stop(self):
        self.tmf = time.localtime()

        print("stop!")
        self._calc()
    def _calc(self):
        self.prompt = "总共运行了"
        self.lasted = self.tmf - self.tms
        self.prompt += str(self.lasted)
        print(self.prompt)

