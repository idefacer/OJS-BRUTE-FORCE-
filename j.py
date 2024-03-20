import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style

paths = [
    "/files/",
    "/file/",
    "/journals/",
    "/journal/",
    "/jurnal/",
    "/jurnals/",
    "/jurnal_file",
    "/jurnal_files/",
    "/jurnal_data_file/",
    "/jurnal_data_files/",
    "/jurnalfile/",
    "/jurnal_dat0_file/",
    "/jurnalfiles/",
    "/jurnaldatafile/",
    "/jurnaldatafiles/",
    "/data/",
    "/ojsfiles/journals/",
    "/datafile/",
    "/datafiles/",
    "/journalfile/",
    "/journalfiles/",
    "/journal_file/",
    "/journal_files/",
    "/journal_data/",
    "/journal_data_file/",
    "/journal_data_files/"
]

def scan_path(url, path):
    try:
        full_url = url + path
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"{Fore.GREEN}Path ditemukan: {full_url}")
            if "Index of" in response.text:
                print(f"  - Index of ditemukan di: {full_url}")
            if "vulnerable" in response.text.lower():
                print(f"  - Pesan kerentanan ditemukan di: {full_url}")
        else:
            print(f"{Fore.RED}Path tidak ditemukan: {full_url}")
    except Exception as e:
        print(f"{Fore.RED}Error:", e)

def fast_scan(url):
    try:
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Memindai setiap path dengan menggunakan executor
            executor.map(lambda path: scan_path(url, path), paths)
    except Exception as e:
        print(f"{Fore.RED}Error:", e)

def main():
    url = input("URL [ https://domain.com ] : ")
    fast_scan(url)

if __name__ == "__main__":
    main()
