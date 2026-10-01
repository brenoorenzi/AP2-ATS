import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestExercicio01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        caminho_arquivo = os.path.abspath("exercicio01.html")
        self.driver.get(f"file:///{caminho_arquivo}")

    def test_a_verificar_titulo(self):
        titulo = self.driver.title
        print(f"\n[Item A] Título da página: {titulo}")
        self.assertEqual(titulo, "Exercício 01")

    def test_b_verificar_paragrafo_tag_name(self):
        elemento_p = self.driver.find_element(By.TAG_NAME, "p")
        print(f"[Item B] Conteúdo via TAG_NAME: {elemento_p.text}")
        self.assertEqual(elemento_p.text, "O conteúdo do site vem aqui")

    def test_c_verificar_paragrafo_css_selector(self):
        elemento_css = self.driver.find_element(By.CSS_SELECTOR, "p.content")
        print(f"[Item C] Conteúdo via CSS_SELECTOR: {elemento_css.text}")
        self.assertEqual(elemento_css.text, "O conteúdo do site vem aqui")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()