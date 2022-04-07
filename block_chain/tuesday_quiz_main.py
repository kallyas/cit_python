from tuesday_quiz import *

rows = ["Bread", "Milk", "Eggs", "Cheese", "Butter", "Coffee", "Tea"]
columns = [3500, 9000, 2000, 5000, 8000, 4000, 3000]

store_chart = Store_Chart(rows, columns)

store_chart.plot_chart()

df = store_chart.data_frame()

plot_graph = Plot_Graph()

plot_graph.plot_graph(data=df, labels=rows)
plt.show()

github_logo = "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png"
img = download_image(github_logo)
resized_img = resize_image(img, width=300)
show_image(img, resized_img)


def send_money(sender, recipient, amount):
    data = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    res = requests.post('http://localhost:5000/send-money', data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(res.json())


def recieve_money(recipient):
    data = {
        'recipient': recipient
    }

    res = requests.post('http://localhost:5000/recieve-money', data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(res.json())

def deposit_money(amount):
    data = {
        'recipient': 'iden',
        'amount': amount,
        'sender': 'iden'
    }

    res = requests.post('http://localhost:5000/deposit-money', data=json.dumps(data), headers={'Content-Type': 'application/json'})
    print(res.json())


while True:
    print("""
    1. Send money
    2. Recieve money
    3. Deposit money
    4. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        sender = input("Enter your name: ")
        recipient = input("Enter recipient name: ")
        amount = int(input("Enter amount: "))
        send_money(sender, recipient, amount)
    elif choice == "2":
        recipient = input("Enter recipient name: ")
        recieve_money(recipient)
    elif choice == "3":
        amount = int(input("Enter amount: "))
        deposit_money(amount)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
