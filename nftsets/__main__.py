from image_sets import ImageSet


def main():
    image_set = ImageSet("config.json")
    image_set.build_set()


if __name__ == "__main__":
    main()
