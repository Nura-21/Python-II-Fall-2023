
print(*[input().replace("&&", "and").replace("||", "or")
      for _ in range(int(input()))], sep='\n')
