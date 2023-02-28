def make_string(s):
    words = s.split()
    return ''.join([word[0] for word in words])

if __name__ == '__main__':
    print(make_string('sees eyes xray yacht Q'))