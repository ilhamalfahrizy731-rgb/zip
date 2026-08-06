import cv2
import os

def extract_all_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print("Gagal membuka file video!")
        return

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frame yang akan diekstrak: {total_frames}")

    frame_count = 0

    while True:
        # cap.read() membaca frame demi frame secara berurutan
        ret, frame = cap.read()
        
        # Jika video sudah habis, hentikan loop
        if not ret:
            break

        # Format nama file: frame_0001.jpg, frame_0002.jpg, dst.
        frame_name = os.path.join(output_folder, f"frame_{frame_count:05d}.jpg")
        
        # Simpan frame dengan kualitas JPEG tinggi (95%)
        cv2.imwrite(frame_name, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
        
        frame_count += 1
        
        # Tampilkan progress sederhana
        if frame_count % 100 == 0:
            print(f"Progress: {frame_count}/{total_frames} frame tersimpan...")

    cap.release()
    print(f"Selesai! Total {frame_count} frame berhasil disimpan ke folder '{output_folder}'.")

# Jalankan skrip
extract_all_frames('lamborghini.mp4', 'output_all_frames')