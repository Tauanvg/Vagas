class itens:
    pesquisa = None

    def __init__(self):
        self.termos = ['computação', 'informação', 'Python', 'JavaScript', 'backend', 'linguage', 'Programação',
                       'software', 'Sistema', 'SQL', 'Tecnologia', 'SAP', 'Service Now', 'Jira',
                       'Java', 'dados', 'Dados', 't.i', 'Software', 'T.I.',
                       'Redes', 'Programador', 'informática', 'Computação', 'Dev', 'RPA', 'Front-End', 'ERP', 'Business Intelligence',
                       'Computacao', 'infraestrutura', 'Help Desk',
                       ]
        self.url = [
            'https://portal.gupy.io/vagas?searchTerm=estagio&state=rioDeJaneiro&remoteWorking=not-remote',
            'https://portal.gupy.io/vagas?searchTerm=estagio&remoteWorking=only-remote',
            'https://www.vagas.com.br/vagas-de-estagio?m%5B%5D=100%25+Home+Office',
            'https://www.linkedin.com/jobs/search/?f_TPR=r604800&f_WT=2&geoId=106057199&keywords=estagiar&location=Brasil&sortBy=R',
            #'https://www.google.com/search?q=estagio&client=opera&hs=dht&ei=PPPKYZe3EevR1sQP6_6IyAo&uact=5&oq=estagio&gs_lcp=Cgdnd3Mtd2l6EAMyCwgAEIAEELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyDggAEIAEELEDEIMBEMkDMgUIABCSAzIFCAAQkgMyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEOgcIABBHELADSgQIQRgASgQIRhgAUMIGWL0HYPgIaAJwAXgAgAGOAYgB-gGSAQMwLjKYAQCgAQHIAQjAAQE&sclient=gws-wiz&ibp=htl;jobs&sa=X&ved=2ahUKEwix4aexsIb1AhUDq5UCHcc8C48QudcGKAJ6BAgTECg#fpstate=tldetail&htivrt=jobs&htidocid=r8JS7o7uQb8dDX6uAAAAAA%3D%3D',

        ]
        self.pesquisa = [#'tecnologia',
                         'internship',
                         'intern',
                         'estagio',
                         'estagiario',
                         ]
        self.pesquisaavancada = [
                        ' Rio de janeiro',
                        ' Remoto'
        ]
        self.negativo = [
            'publicidade', 'ADMINISTRATIVO', 'RECURSOS HUMANOS', 'Direito', 'Administração', 'Administrativa',
            'Comunicação', 'Marketing', 'Personalização', 'ao público', 'marketing', 'de Produção',
            'direito', 'Arquitetura', 'MARKETING', 'Pedagogia', 'Pessoal', 'RH', 'Elétrica', 'MÉDIO', 'Industrial',
            'Comercial', 'vendas', 'Desenho', 'Executivo', 'Publicidade', 'Auditoria', 'Cobrança',
            'Audiovisual', 'Jurídico', 'Técnico', 'Administrativo', 'Hotelaria', 'Turismo', 'contábeis', 'Vendas',
            'CONTROLADORIA', 'audiovisual','Sonoros', 'Materiais', 'Obra', 'Nutrição', 'Atendimento',
            'Design', 'Estética', 'Propaganda', 'fisioterapia', 'Gráfico', 'serviços gerais', 'Contábil', 'Conteúdo',
            'Farmácia', 'Analista', 'Compras', 'Gastronomia', 'Mídia', 'Faturamento', 'Financeiro', 'Recruiter',
            'humanos', 'recursos', 'edificações', 'Ensino', 'Sociais', 'COMERCIO', 'Recepção', 'Social Media',
            'Cível', 'Contencioso', 'Gente', 'Licenciatura', 'Imobiliário', 'Engajamento', 'Novos Negócios', 'Product Owner',
            'Contabilidade', 'Logística', 'Luxo', 'Recrutamento', 'Seleção', 'Enfestador', 'Separador', 'Civil', 'Relacionamento',
            'TRANSPORTES', 'Letras', 'Trading', 'Tesouraria', 'Construção', 'Barragens', 'Disciplina', 'Microbiologia',
            'Representative', 'de Empresas', 'Owner', 'Física', 'Trabalhista', 'Suprimentos', 'Coleta', 'Auxiliar',
            'GQP', 'Societário', 'MECÂNICA', 'ORÇAMENTOS', 'Prospecção', 'Saúde', 'FABRICAÇÃO', 'Social', 'Contabeis',
            'Agronomia', 'Frotas', 'Aprendiz', 'Eventos', 'Fotografia', 'Pessoas com Deficiência', 'Educação',
            'Química', 'do Trabalho', 'PCD', 'Escrita', 'Gestão de Processos', 'Escrita', 'Didática', 'Musical',
            'Vendedor', 'Meio Ambiente', 'Especialista', 'Master', 'Gerente', 'Consultor', 'Engineer', 'Distribuição',
            'Gpex', 'de Documentos', 'Interno', 'Advogado', 'Motorista', 'Enfermagem','Ambulatório', 'Biologia',
            'Enfermeiro', 'Pleno', 'Sênior', 'Contas', 'Estoque', 'Escola', 'Eletrônica', 'Benefícios', 'Laboratório',
            'Demanda', 'Rodovias', 'Financeira', 'Documentos', 'Manutenção', 'Corretor', 'Imóveis', 'Conferente',
            'MUSCULAÇÃO', 'GINÁSTICA', 'Acquisition', 'Talent', 'Negras', 'Pro Bono ', 'Enfermeiro', 'Sr.',
            'Jurídica', 'Coordenador', 'Consultor', 'Bilíngue', 'Consultant', 'Imobiliári', 'BIM', 'Dev Ops',
            'Urbano', 'Call', 'Sales', 'Human Resources', 'Comprador', 'Cinema', 'Plena', 'Redator', 'Patrocínio',
            'Atendente', 'lanchonete', 'Modelo', 'de Prova', 'Editor', 'Vídeo', 'CAD', 'Modelagem', 'Modelista',
            'Cortador', 'Lead', ' Sr ', 'Pessoas', 'e Cultura', 'Biblioteconomia', 'Estilista', 'Ambiental', 'Ateliê',
            'Contencioso', 'Contabilidade', 'Audiovisual', 'Hotelaria', 'Turismo', 'Contábil', 'Marketing',
            'MARKETING', 'Propaganda', 'Jornalismo', 'Materia', 'Conteúdo', 'Compras', 'Marketing', 'Química',
            'RH', 'ADMINISTRAÇÃO', 'MIDIAS SOCIAIS', 'Administra', 'Pedagogia', 'Pessoal', 'Departamento',
            'Compras', 'Farmácia', 'Comercial', 'Vendas', 'Administra', 'CONTÁBEIS', 'Médio', 'RECURSOS HUMANOS',
            'De RH', 'LETRAS', 'EM RH', 'De Pedagogia', 'EM LOGÍSTICA', 'área Administrativa', 'DEPARTAMENTO PESSOAL',
            'MARKETING DE PRODUTO', 'Produção Industrial', 'Administração De Empresas', 'Ciências Contábeis',
            'Comercial', 'EM MARKETING', 'De Direito', 'De Contabilidade', 'MARKETING/E-COMMERCE', 'EM CONTABILIDADE',
            'Produção De Audiovisual', 'Business Center', 'Gestão Comercial', 'Contábil', 'PCD', 'Marketing Digital',
            'Produção De Conteúdo', 'De Compras', 'Engenharia Química', 'DE MARKETING', 'De RH', 'Emprego', 'OEmprego',
            'MARKETING PARA CONTEUDOS', 'De Pedagogia', 'Em Farmácia', 'Em Vendas','Pleno', 'RISCO'
            'Fullstack', 'Coordenador', 'Gerente', 'Auditor', 'Pricing' 'Mineração', 'Revenue', 'Operações',
            'Suporte ao Cliente', 'Compliance', 'Treinamento', 'Tributário', 'Telecom', 'Diversidade',
            'finanças', 'Entrega', 'Supervisor', 'Pricing', 'Engenharia de Processos', 'Psicologia', 'Business & Finance'
            'Transformation', 'E-Commerce', 'P&D', 'em Qualidade', 'Teatro', 'Drama', 'ORIENTADOR', 'Elétric', 'Incêndio',
            'Combate','Logistics', 'Líder', 'Account', 'Manager', 'Planejamento', 'FUNDOS', 'Financiamento', 'desenvolvedor',
            'DevOps', 'Developer', 'senior', 'Gestor', 'Automatizador', 'Architect', 'Arquiteto'
        ]
        self.Positivos = [
            'Summer', 'remote', 'Estágio', 'Estagiário',
        ]
        self.PositivosF = [
            ' em ', ' na ', ' da ', ' de ',
        ]
        self.negativoS = [
            'OEmprego', 'Vaga', 'Abre', 'Emprego', 'Jobbol', 'carrer', 'Netvagas.com.br', 'Divulga'
        ]


    @classmethod
    def Negativo(cls, nome):
        for negativoI in itens().negativo:
            if nome.upper().find(negativoI.upper()) >= 0:
                print(nome, '--->', negativoI)
                return True
        return False

    @classmethod
    def Positivo(cls, nome):
        for negativoF in itens().PositivosF:
            if nome.upper().find(negativoF.upper()) < 0:
                print(nome, '--->', negativoF)
                return False
        for negativoI in itens().Positivos:
            if nome.upper().find(negativoI.upper()) >= 0:
                print('\n',nome, '--->', negativoI,'\n')
                return True
        return False

    @classmethod
    def NegativoS(cls, nome, vaga):
        for negativoI in itens().negativoS:
            if nome.upper().find(negativoI.upper()) >= 0:
                print(vaga, '--->', negativoI)
                return True
        return False

    @classmethod
    def VRF(cls, nome):
        teste = 0
        for termo in itens().termos:
            if nome.upper().find(termo.upper()) >= 0:
                teste += 1
                break
        if teste >= 1:
            return True
        else:
            return False

    @classmethod
    def VRFC(cls, nome):
        teste = 0
        for termo in itens().termos:
            if nome.upper().find(termo.upper()) >= 0:
                teste += 1
                break
        if teste >= 4:
            return True
        else:
            return False

