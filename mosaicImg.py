import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
import cv2
import cvlib

class faomWindow:
    def __init__(self):
        # 프레임 기본 설정
        self.root = tk.Tk()
        self.root.title('face and object mosaic')
        self.root.iconbitmap('mosaicImg_icon.ico')
        self.root.geometry('510x390')
        self.root.resizable(False, False)
        
        # 필드 값 초기화
        self.filepath = ''
        self.rate = tk.IntVar()
        self.rate.set(15)
        self.fps = tk.IntVar()
        self.fps.set(20)
        self.proc_opt = tk.IntVar()
        self.proc_opt.set(1)
        self.stickerpath = ''
        self.box_color = '#000000'
        
        # 상단 파일 찾는 부분
        self.top_frame = tk.Frame(self.root, height=20, relief='solid', bd=1)
        self.label_filepath = tk.Label(self.top_frame, width=50, borderwidth=3, relief="sunken", text=self.filepath)
        self.label_filepath.grid(column=0, row=0, padx=10, pady=20)
        self.get_file_btn = tk.Button(self.top_frame, text='파일 찾기', command=self.fileLoad)
        self.get_file_btn.grid(column=1, row=0, padx=10, pady=20)
        
        # 중단 설정하는 부분
        self.middle_frame = tk.Frame(self.root, height=20, relief='solid', bd=1)
        self.label_rate = tk.Label(self.middle_frame, width=5, text='rate : ')
        self.label_rate.grid(column=0, row=0, sticky='e', padx=10, pady=10)
        self.entry_mosaic_rate = tk.Entry(self.middle_frame, width=8, borderwidth=2, text=self.rate)
        self.entry_mosaic_rate.grid(column=1, row=0, sticky='w', pady=10)
        self.label_fps = tk.Label(self.middle_frame, width=5, text='fps : ')
        self.label_fps.grid(column=2, row=0, sticky='e', padx=10, pady=10)
        self.entry_video_fps = tk.Entry(self.middle_frame, width=8, borderwidth=2, text=self.fps)
        self.entry_video_fps.grid(column=3, row=0, sticky='w', pady=10)
        # 변경할 옵션 선택1 (모자이크)
        self.proc_opt_1 = tk.Radiobutton(self.middle_frame, text='mosaic', value=1, variable=self.proc_opt, command=self.optSelect)
        self.proc_opt_1.grid(column=0, row=1, sticky='w', padx=15)
        self.proc_opt_1.select()
        # 변경할 옵션 선택2 (스티커)
        self.proc_opt_2 = tk.Radiobutton(self.middle_frame, text='sticker', value=2, variable=self.proc_opt, command=self.optSelect)
        self.proc_opt_2.grid(column=0, row=2, sticky='w', padx=15)
        self.label_stickerpath = tk.Label(self.middle_frame, width=30, borderwidth=3, relief="sunken", text=self.stickerpath, state=tk.DISABLED)
        self.label_stickerpath.grid(column=1, row=3, sticky='w', columnspan=2)
        self.get_stf_btn = tk.Button(self.middle_frame, text='파일 찾기', command=self.stickerLoad, state=tk.DISABLED)
        self.get_stf_btn.grid(column=3, row=3, sticky='w', padx=10)
        # 변경할 옵션 선택3 (배경색)
        self.proc_opt_3 = tk.Radiobutton(self.middle_frame, text='color', value=3, variable=self.proc_opt, command=self.optSelect)
        self.proc_opt_3.grid(column=0, row=4, sticky='w', padx=15)
        self.label_bg_color = tk.Label(self.middle_frame, width=8, height=1, relief="sunken", borderwidth=3, bg=self.box_color, state=tk.DISABLED)
        self.label_bg_color.grid(column=1, row=5, sticky='w')
        self.get_color_btn = tk.Button(self.middle_frame, text='Select a Color', command=self.changeColor, state=tk.DISABLED)
        self.get_color_btn.grid(column=3, row=5, sticky='w', padx=15)
        
        # 하단 파일 처리하는 부분
        self.bottom_frame = tk.Frame(self.root, height=20, relief='solid', bd=1)
        self.proc_btn = tk.Button(self.bottom_frame, width=60, height=2, text='process', command=self.clickProcBtn)
        self.proc_btn.pack(fill='none', expand=True, pady=10)
        
        # 프레임 등록
        self.top_frame.pack(fill='x', padx=20, pady=10)
        self.middle_frame.pack(fill='x', padx=20, pady=10, ipady=10)
        self.bottom_frame.pack(fill='x', padx=20, pady=10)
        self.root.mainloop()
        
        
    # 파일 로드
    def fileLoad(self):
        filename = filedialog.askopenfilename(initialdir="./", title="Select file",
                                                  filetypes=(("all files", "*.*"),
                                                             ("image files", "*.jpg;*.jpeg;*.png"),
                                                             ("video files", "*.mp4")))
        self.label_filepath.config(text=filename)
        self.filepath = filename
    
    # 스티커 파일 로드
    def stickerLoad(self):
        filename = filedialog.askopenfilename(initialdir="./", title="Select file",
                                                  filetypes=(("all files", "*.*"),
                                                             ("image files", "*.jpg;*.jpeg;*.png")))
        self.label_stickerpath.config(text=filename)
        self.stickerpath = filename
    
    # 편집할 옵션 선택
    def optSelect(self):
        opt = self.proc_opt.get()
        if opt == 1:
            self.label_stickerpath.config(state=tk.DISABLED)
            self.get_stf_btn.config(state=tk.DISABLED)
            self.label_bg_color.config(state=tk.DISABLED)
            self.get_color_btn.config(state=tk.DISABLED)
        elif opt == 2:
            self.label_stickerpath.config(state=tk.NORMAL)
            self.get_stf_btn.config(state=tk.NORMAL)
            self.label_bg_color.config(state=tk.DISABLED)
            self.get_color_btn.config(state=tk.DISABLED)
        elif opt == 3:
            self.label_stickerpath.config(state=tk.DISABLED)
            self.get_stf_btn.config(state=tk.DISABLED)
            self.label_bg_color.config(state=tk.NORMAL)
            self.get_color_btn.config(state=tk.NORMAL)
    
    # 색깔박스의 색 선택
    def changeColor(self):
        colors = askcolor(title="Tkinter Color Chooser")
        self.label_bg_color.config(bg=colors[1])
        self.box_color = colors
    
    # 이미지 모자이크
    def procMosaicImage(self):
        rate = self.rate.get()
        p_opt = self.proc_opt.get()
        img = cv2.imread(self.filepath)
        
        faces, confidences = cvlib.detect_face(img)
        for face,conf in zip(faces,confidences):
            # 편집할 위치
            (startX,startY) = face[0],face[1]
            (endX,endY) = face[2],face[3]
            w = endX - startX
            h = endY - startY
            
            # 모자이크 처리 (option=1)
            if p_opt == 1:
                roi = img[startY:endY, startX:endX]
                roi = cv2.resize(roi, (w//rate, h//rate))
                roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
                img[startY:endY, startX:endX] = roi
            # 스티커 처리 (option=2)
            elif p_opt == 2:
                stic_img = cv2.imread(self.stickerpath)
                stic_img = cv2.resize(stic_img, (w, h))
                img[startY:endY, startX:endX] = stic_img
            # 색깔박스 처리 (option=3)
            elif p_opt == 3:
                cv2.rectangle(img, (startX,startY), (endX,endY), (0,255,0), -1)
                
        a = cv2.imwrite('result.jpg', img)
        print(a)

    
    # 동영상 모자이크
    def procMosaicVideo(self):
        rate = self.rate.get()
        fps = self.fps.get()
        p_opt = self.proc_opt.get()
        color = self.box_color[0]
        cap = cv2.VideoCapture(self.filepath)
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter('result.avi', fourcc, fps, (round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
        if cap.isOpened():
            while True:
                ret, img = cap.read()                        
                if ret:     
                    faces, confidences = cvlib.detect_face(img)
                    for face,conf in zip(faces,confidences):
                        # 모자이크 진행하기
                        (startX,startY) = face[0],face[1]
                        (endX,endY) = face[2],face[3]
                        w = endX - startX
                        h = endY - startY
                        if startX<0 or endX>img.shape[1] or startY<0 or endY>img.shape[0]:
                            continue

                        # 모자이크 처리 (option=1)
                        if p_opt == 1:
                            roi = img[startY:endY, startX:endX]
                            roi = cv2.resize(roi, (w//rate, h//rate))
                            roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
                            img[startY:endY, startX:endX] = roi
                        # 스티커 처리 (option=2)
                        elif p_opt == 2:
                            stic_img = cv2.imread(self.stickerpath)
                            stic_img = cv2.resize(stic_img, (w, h))
                            img[startY:endY, startX:endX] = stic_img
                        # 색깔박스 처리 (option=3)
                        elif p_opt == 3:
                            cv2.rectangle(img, (startX,startY), (endX,endY), (color[2], color[1], color[0]), -1)
                    out.write(img)
                else:                 
                    break 
        else:
            print("can't open video.")
            cap.release()
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    
    # 처리 버튼 클릭
    def clickProcBtn(self):
        p = self.proc_opt.get()
        ftype = self.filepath.split('.')[-1]
        
        if ftype=='mp4':
            self.procMosaicVideo()
        else:
            self.procMosaicImage()
            

if __name__ == '__main__':
    faomWindow()