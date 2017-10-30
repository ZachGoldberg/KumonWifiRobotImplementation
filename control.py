import socket
import binascii
import time
import sys
BOT_IP = '192.168.1.1'
BOT_PORT = 2001

SOCK = None


def send_command(cmd, subcmd, arg):
  print "Sending %s %s %s" % (cmd, subcmd, arg)
  SOCK.send(binascii.a2b_hex('ff'))
  SOCK.send(binascii.a2b_hex(cmd))
  SOCK.send(binascii.a2b_hex(subcmd))
  SOCK.send(binascii.a2b_hex(arg))
  SOCK.send(binascii.a2b_hex('ff'))


def stop():
  send_command('00', '00', '00')

def forwards(sec):
  send_command('00', '02', '00')
  time.sleep(sec)
  stop()

def backwards(sec):
  send_command('00', '01', '00')
  time.sleep(sec)
  stop()

def left(sec):
  send_command('00', '03', '00')
  time.sleep(sec)
  stop()

def right(sec):
  send_command('00', '04', '00')
  time.sleep(sec)
  stop()

def camera_v(angle):
  val = angle
  send_command('01', '08', val)

def camera_h(angle):
  val = angle
  send_command('01', '07', val)


def init():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((BOT_IP, BOT_PORT))
  global SOCK
  SOCK = s

if __name__ == '__main__':

  init()
  camera_1(100)
  #forwards(1)
  #time.sleep(0.5)
  #backwards(1)
  SOCK.close()
