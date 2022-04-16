import shutil
import logging
import ipaddress

import luigi


class TargetList(luigi.ExternalTask):
    target_file = luigi.Parameter()
    target = luigi.Parameter()
    date = luigi.DateParameter()
    def output(self):
        try:
            with open(self.target_file) as file:
                line = file.readline()
                ipaddress.ip_interface(line.strip())
        except OSError as e:
            logging.error(e)
        except ValueError as e:
            logging.error(e)
            with_suffix = f"{self.target_file}.domains"
        else:
            with_suffix = f"{self.target_file}.ips"
        shutil.copy(self.target_file, with_suffix)  
        logging.info(f"Copied {self.target_file} to {with_suffix}")
        return luigi.LocalTarget(with_suffix)
    
