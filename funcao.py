import cv2
import numpy


def lendo_imagem():
    # Leitura da imagem com a função imread()
    imagem = cv2.imread('imagem.jpg', 1)
    cv2.imshow('Mostrando uma imagem', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def coordenadas():
    imagem = cv2.imread('imagem.jpg')
    (b, g, r) = imagem[0, 0]  # veja que a ordem BGR e não RGB
    print('O pixel (0, 0) tem as seguintes cores: ')
    print('Vermelho:', r, 'Verde:', g, 'Azul:', b)


def mod_azul():
    imagem = cv2.imread('imagem.jpg')
    for y in range(0, imagem.shape[0]):
        for x in range(0, imagem.shape[1]):
            imagem[y, x] = (255, 0, 0)
    cv2.imshow("Imagem modificada", imagem)


def larg_alt():
    imagem = cv2.imread('imagem.jpg')  # Leitura da imagem com a função imread()
    print('Largura em pixels: ', end='')
    print(imagem.shape[1])  # largura da imagem
    print('Altura em pixels: ', end='')
    print(imagem.shape[0])  # altura da imagem
    print('Qtde de canais: ', end='')
    print(imagem.shape[2])
    cv2.waitKey(0)
