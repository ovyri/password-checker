from datetime import datetime

def verificar_password(password):
    # Paso 2: Procesamiento lógico con condiciones (if / else)
    if len(password) < 8:
        return "INSEGURA (Muy corta, menos de 8 caracteres)"
    else:
        return "SEGURA (Cumple con el largo mínimo de 8 caracteres)"

if __name__ == "__main__":
    # Paso 1: La Entrada (input)
    print("--- Verificador de Fortaleza de Contraseñas ---")
    password_usuario = input("Ingresá la contraseña a evaluar: ").strip()
    
    if not password_usuario:
        print("[!] No ingresaste ninguna contraseña.")
    else:
        # Ejecutamos la lógica
        veredicto = verificar_password(password_usuario)
        
        # Mostramos la salida en pantalla (print)
        print(f"\n[+] Resultado: {veredicto}")
        
        # Paso 3: Guardar el reporte en un archivo .txt (file.write)
        # (¡Igual que hicimos en el escáner de puertos!)
        fecha_actual = datetime.now()
        reporte_texto = f"Fecha: {fecha_actual}\nContraseña evaluada: {password_usuario}\nEstado: {veredicto}\n" + "-"*40 + "\n"
        
        with open("reporte_senias.txt", "a", encoding="utf-8") as f:
            f.write(reporte_texto)
            
        print("[i] Resultado guardado en 'reporte_senias.txt'")