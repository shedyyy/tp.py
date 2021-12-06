import time
seconde=int(input("Saisir un nombre entier n positif: "))

for i in range(seconde) :
    seconde = seconde - 1
    time.sleep(1)
    print(seconde)
