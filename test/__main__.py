from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_arg('name', default='World')
    args = parser.parse_args()
    print(f"Hello, {args.name}!")
