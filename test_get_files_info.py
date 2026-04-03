from functions.get_files_info import get_files_info


def main():
    target_dirs = ['.', 'pkg', '/bin', '../']
    for td in target_dirs:
        print(f"Result for '{td}' directory:")
        print(get_files_info("calculator", td))
        print()

if __name__ == "__main__":
    main()
