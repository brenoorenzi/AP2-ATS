import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_html = "file://" + os.path.join(diretorio_atual, "avaliacao.html")
driver.get(caminho_html)

time.sleep(1)

campo_nome = driver.find_element(By.ID, "nome")
campo_nome.send_keys("Brenorenzi")
time.sleep(0.8)

campo_ra = driver.find_element(By.ID, "ra")
campo_ra.send_keys("2403703")
time.sleep(0.8)

campo_dia = driver.find_element(By.ID, "dia")
campo_dia.send_keys("18")
time.sleep(0.8)

campo_mes = driver.find_element(By.ID, "mes")
campo_mes.send_keys("09")
time.sleep(0.8)

campo_ano = driver.find_element(By.ID, "ano")
campo_ano.send_keys("2005")
time.sleep(0.8)

lista_curso = Select(driver.find_element(By.ID, "curso"))
lista_curso.select_by_visible_text("Análise e Desenvolvimento de Sistemas")
time.sleep(0.8)

lista_aproveitamento = Select(driver.find_element(By.ID, "aproveitamento"))
lista_aproveitamento.select_by_visible_text("10")
time.sleep(0.8)

campo_sugestoes = driver.find_element(By.ID, "sugestoes")
campo_sugestoes.send_keys("Gostei muito do conteúdo. Sugiro mais atividades práticas interativas no desenvolvimento das aulas.")
time.sleep(0.8)

campo_obs = driver.find_element(By.ID, "observacoes")
campo_obs.send_keys("Sem mais observações.")
time.sleep(0.8)

botao_enviar = driver.find_element(By.ID, "enviarFeedback")
botao_enviar.click()
time.sleep(0.8)

time.sleep(10)

driver.quit()