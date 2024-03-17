import login
import register



def main():
    services = input("""
    1. Login
    2. Register
            >>>""")

    if services == "1":
        return login.login()

    elif services == "2":
        return register.register()
    else:
        print("\nError\n")
        return main()


if __name__ == "__main__":
    main()