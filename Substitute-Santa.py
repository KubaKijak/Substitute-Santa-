print("hej, skriv det namn och vad du önskar dig i jul")


options = list()
genre = input("Önskelista: ")
option = ""
count = 1
while option != "done":
   option = input("Option "+str(count)+": ")
   if option != "done":
      options.append(option)
      count += 1

with open(genre+'.txt', 'w+') as text_file:
  text_file.write("\n".join(options))