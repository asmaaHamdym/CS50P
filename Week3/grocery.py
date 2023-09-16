items =[]
dict={}
def main():
    while True:
        try:
            items.append(input().upper())
        except EOFError:
            list=sorted(items)
            for i in range(len(list)):
                dict[list[i]]=list.count(list[i])
            for j in dict:
                print(dict[j],j)
            break
        except (KeyError):
            pass
main()