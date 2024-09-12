# YOLO Image Treatments

Este repositório oferece uma série de scripts e ferramentas para o pré-processamento e tratamento avançado de imagens e vídeos, com um foco especial na integração com modelos YOLO para detecção de objetos. Este repositório é projetado para fornecer uma gama de funcionalidades que melhoram ou adaptam a qualidade das imagens e vídeos, facilitando a análise e o treinamento de modelos de visão computacional.

## Funcionalidades

Este repositório contém uma coleção de scripts e ferramentas para o tratamento e processamento de imagens e vídeos, com foco na integração com modelos YOLO para detecção de objetos. Os principais recursos incluem:

- [ ] **Corte de Imagens**: Funções para realizar o recorte de regiões específicas em imagens com base em coordenadas definidas ou em áreas detectadas por modelos de detecção de objetos.
  
- [x] **Extração de Frames de Vídeos**: Scripts para extrair frames de vídeos em intervalos específicos, possibilitando a análise de vídeos quadro a quadro ou a preparação de conjuntos de dados para treinamento de modelos.

- [ ] **Rotacionamento de Imagens**: Ferramentas para rotacionar imagens em ângulos definidos, úteis para data augmentation ou correção de orientação.

- [ ] **Ajuste de Brilho e Contraste**: Ferramentas para ajustar o brilho e o contraste das imagens, melhorando a visibilidade dos objetos e ajudando na generalização do modelo.

- [ ] **Correção de Cor**: Funções para ajustar o balanço de cores e corrigir variações na iluminação, garantindo que as imagens estejam em um formato consistente para o modelo YOLO.

- [ ] **Redução de Ruído**: Aplicação de filtros para reduzir o ruído das imagens, melhorando a precisão da detecção de objetos e a qualidade dos dados.

- [ ] **Preto e Branco**: Funções para converter imagens em escala de cinza, o que pode ser útil para determinadas análises ou para simplificar o processamento.

- [x] **Aumento de Velocidade de Vídeo**: Scripts para acelerar a reprodução de vídeos em um fator especificado, útil para análise rápida ou para simulação de condições de alta velocidade.

- [ ] **Integração com YOLO**: Exemplos de como utilizar os tratamentos de imagem em conjunto com o YOLO para melhorar o pré-processamento de dados e a interpretação dos resultados.


## Requisitos

- Python 3.x
- OpenCV
- NumPy

Instale as dependências com:

```bash
pip install opencv-python numpy
