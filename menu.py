from scraper import opentunnel, pisovpn, sshocean, vpnjantit
from tester.socket_tester import is_server_reachable

def harvest_vless():
    print("\n[*] Harvesting VLESS configs from providers...\n")
    all_links = set()

    for scraper in [opentunnel, pisovpn, sshocean, vpnjantit]:
        try:
            links = scraper.fetch_vless_links()
            print(f"[+] {scraper.__name__}: {len(links)} configs fetched.")
            all_links.update(links)
        except Exception as e:
            print(f"[-] Failed {scraper.__name__}: {e}")

    print(f"\n[*] Testing {len(all_links)} servers...")
    working = [link for link in all_links if is_server_reachable(link)]

    print(f"\n✅ {len(working)} Working Configs:\n")
    for link in working:
        print(link)

    print("\n[*] Done.\n")

def main_menu():
    while True:
        print("\n=== VLESS Harvester ===")
        print("1. Harvest and test VLESS configs")
        print("2. (Reserved) Export working configs to file")
        print("3. (Reserved) Use xray-core to validate")
        print("0. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            harvest_vless()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")