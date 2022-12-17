class Tag:
    def __init__(self, name, **attrs):
        self.name = name.upper()
        self.attrs = attrs

    def __enter__(self):
        attr_list = [key + '=' + f'"{value}"' for key, value in self.attrs.items()]
        attr_list.insert(0, self.name)
        contents = ' '.join(attr_list)
        print(f'<{contents}>')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'</{self.name}>')


if __name__ == '__main__':
    with Tag('html'):
        with Tag('head'), Tag('title'):
            print('Simple HTML')
        with Tag('body', color='white', width='80%'):
            print('Hello World')
