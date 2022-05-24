import ReplicatorSender
import rpyc

def open_connection():
    #connecting to ReplicatorSenderService
    conn = rpyc.connect("localhost", 22277)
    conn.on_connect()
    print("Writer connected.")
    return conn

def close_connection(conn):
    #disconnecting from ReplicatorSenderService
    conn.on_disconnect()
    #command for disconnecting
    print("Writer disconnected.")
