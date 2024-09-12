import cv2


def display_accelerated_video(video_path, speed_up_factor=10):
    # Abre o vídeo original
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return
    
    # Obtém informações do vídeo
    fps = cap.get(cv2.CAP_PROP_FPS)  # FPS original
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # Largura dos frames
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # Altura dos frames

    # Define o novo FPS
    new_fps = fps * speed_up_factor
    
    # Calcula o intervalo de exibição dos frames
    delay = int(1000 / new_fps)  # Em milissegundos

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Mostra o frame
        cv2.imshow('Vídeo Acelerado', frame)

        # Espera pela tecla 'q' para sair ou pela duração do delay
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

        frame_count += 1

    # Libera os objetos
    cap.release()
    cv2.destroyAllWindows()

# Exemplo de uso
video_path = '2024-09-12 15-32-28.mp4'  # Caminho do vídeo original
display_accelerated_video(video_path, speed_up_factor=30)
