from isb.config import settings


def main() -> None:
    print(f"Hello from isb in {settings.ENV} mode!")


if __name__ == "__main__":
    main()
