def send_data(conn, data):
    conn.root.send_to_reader(data)
