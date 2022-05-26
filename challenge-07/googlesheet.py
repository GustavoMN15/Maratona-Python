import gspread
import os

def sheet(jobs):
  gc = gspread.service_account(filename="credentials.json")
  sh = gc.open_by_key('1RBiuxMxBZagCVPGS4XoYSzqkTeq1flJsuL3eZvtRXbc')
  worksheet = sh.sheet1
  contador = 1
  for job in jobs:
    try:
      worksheet.append_row(list(job.values()))
      os.system('clear')
      print(contador,"/",len(jobs),"Enviado!")
      contador = contador + 1
    except:
      print(contador,"/",len(jobs),"ERRO! Limite de cota!")
      contador = contador + 1
      os.system('clear')
        