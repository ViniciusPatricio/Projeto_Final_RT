'''
CREATE TABLE `project_rt`.`clientes` (
  `id_clientes` INT NOT NULL AUTO_INCREMENT,
  `nome_completo` VARCHAR(45) NULL,
  `matricula` VARCHAR(80) NULL,
  `senha` VARCHAR(45) NULL,
  PRIMARY KEY (`id_clientes`));
'''

class Clientes_DB():

    def __init__(self, db):
        self.db = db;

    def insertClient(self,cliente):
        

