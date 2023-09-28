text = ["  banaènaè  ", "  apple  ", "  kiwi  "]

def split_sentences(data: list[str]) -> list[str]:
  # TODO: Implement based on the given description
  data = [i.strip() for i in data]
  data = [i.encode('ascii', 'ignore').decode('ascii') for i in data]
  return data

print(text)
print(split_sentences(text))