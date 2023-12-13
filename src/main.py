import logging
import os
import logging
from dotenv import load_dotenv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("../tmp/check_aws_resources.log"),
        logging.StreamHandler()
    ]
)


load_dotenv()

# Essas variáveis são carregadas a partir do arquivo '.env' e podem
# ser sobreescritas com variáveis de ambiente
ACCOUNT_ID = os.getenv('ACCOUNT_ID') # Conta root na organização
AWS_DEFAULT_PROFILE = os.getenv('AWS_DEFAULT_PROFILE') # profile que irá assumir a role
AWS_EB_PROFILE = os.getenv('AWS_EB_PROFILE') # profile que irá assumir a role
AWS_PROFILE = os.getenv('AWS_PROFILE') # profile que irá assumir a role
AWS_REGION = os.getenv('AWS_REGION')
USE_ORG_FOR_ACCOUNT_LIST = os.getenv('USE_ORG_FOR_ACCOUNT_LIST') # Valos listar todas as cotontas na organização


def main():
    from dependencyChecker import lambda_handler
    # Esse é o entrypoint da função lambda os parâmetros não são usados
    # na função
    event = None
    context = None
    lambda_handler(event, context)


main()
