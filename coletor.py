import os

import cv2


# Função para salvar frames a cada intervalo de tempo
def save_frames(video_path, output_folder, interval=1):
    # Cria a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Abre o vídeo
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)  # Obtém o FPS do vídeo
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = int(fps * interval)  # Calcula o intervalo de frames para salvar

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Verifica se é o momento de salvar o frame
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            print(f"Salvando {frame_filename} - {saved_frame_count} / {(total_frames / fps)}")
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print("Processamento concluído.")

# Exemplo de uso
video_path = '2024-09-12 15-32-28.mp4'  # Caminho do vídeo
output_folder = 'frames'                 # Nome da pasta para salvar os frames
save_frames(video_path, output_folder, interval=10)  # Salva um frame a cada 1 segundo
