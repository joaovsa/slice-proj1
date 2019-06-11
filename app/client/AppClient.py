for i in range(10):
    # Método POST
    data = {'info': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    r = requests.post('http://192.168.50.2:2377/', json=data)
    print("POST ENVIADO OK > {}".format(r.json()))

    # Método GET
    r = requests.get('http://192.168.50.2:2377/')
    print("GET OK > {}".format(r.json()))