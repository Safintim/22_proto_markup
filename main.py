from staticjinja import Site


def main():
    site = Site.make_site()
    site.render(use_reloader=True)


if __name__ == "__main__":
    main()
