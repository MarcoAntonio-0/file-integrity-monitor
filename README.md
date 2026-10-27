# file-integrity-monitor
Monitor de integridade de arquivos em Python: gera um baseline de hashes SHA-256 e detecta arquivos modificados, novos ou removidos. Projeto educacional de Blue Team / SOC.

File integrity monitor in Python: builds a SHA-256 hash baseline and detects modified, new, and deleted files. Educational Blue Team / SOC project.

# 🛡️ File Integrity Monitor

Monitor de integridade de arquivos escrito em Python. Ele cria um *baseline* com o hash SHA-256 de cada arquivo de uma pasta e, depois, compara o estado atual com esse baseline para detectar arquivos **modificados**, **novos** ou **removidos**.

Projeto educacional criado para praticar conceitos de defesa e monitoramento (Blue Team / SOC), inspirado no módulo de FIM de ferramentas como o Wazuh.

> ⚠️ Use apenas em pastas e sistemas que você administra.
