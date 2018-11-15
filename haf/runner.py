# encoding='utf-8'
import time
from multiprocessing import Process

from haf.busclient import BusClient
from haf.case import HttpApiCase
from haf.result import HttpApiResult


class Runner(Process):
    def __init__(self):
        super().__init__()
        self.daemon = True

    def load(self):
        pass

    def run(self):
        self.bus_client = BusClient()
        while True:
            case_handler = self.bus_client.get_case()
            if not case_handler.empty() :
                case = case_handler.get()
                print(case)
            result = self.bus_client.get_result()
            result.put(HttpApiResult())
            time.sleep(1)