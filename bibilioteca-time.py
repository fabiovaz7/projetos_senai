import time
import sys
import os
import platform


def shutdown():
    sistema = platform.system().lower()

    try:
        # Windows
        if "windows" in sistema:
            os.system("shutdown /s /t 0")

        # Linux ou MacOS
        elif "linux" in sistema or "darwin" in sistema:
            os.system("shutdown now")

        # Sistema não reconhecido
        else:
            print("\nSistema operacional não reconhecido")

    except Exception as e:
        print(f"\nErro ao tentar desligar o PC: {e}")

    # print("O computador será desligado em 10 segundos...")
    # time.sleep(10)

    # shutdown()
    def temporizador_com_shutdown():
        print("=== Temporizador Trolator Tabajara ===\n")
        try:
            entrada = input("\nQuantos segundos até o desligamento?")
            segundos = int(entrada)

            while segundos > 0:
                mins, secs = divmod(segundos, 60)
                timer = f"{mins:02d}:{secs:02d}"

    # Bip nos 10 segundos finais 
                bip = "\a" if 0 < segundos < 10 else ""
                print(f"\r Tempo restante: {timer}{bip}", end="", flush=True)
                time.sleep(1)
                segundos -= 1

                print("\nIniciando desligamento.. Tchau! 🖐️")

                shutdown()
        except ValueError:
            print("\Erro: Por favor, digite apenas número inteiro")
        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
