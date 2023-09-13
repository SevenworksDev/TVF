import click
import os
import time

MAX_FPS = 12

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_tvf_file(file_path, fps):
    try:
        with open(file_path, 'r') as tvf_file:
            frames = tvf_file.read().split("\n==END_FRAME==\n")
            
            for frame in frames:
                clear_screen()
                print(frame)
                time.sleep(1 / min(fps, MAX_FPS))
    except FileNotFoundError:
        click.echo(f"Error: File '{file_path}' not found.")
    except KeyboardInterrupt:
        click.echo("\nPlayback interrupted.")

@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--fps', type=float, default=12.0, help='Frames per second (max 12).')
def main(file_path, fps):
    if fps > MAX_FPS:
        click.echo(f"Warning: FPS cannot exceed {MAX_FPS}. Setting FPS to {MAX_FPS}.")
        fps = MAX_FPS

    click.echo("TVF Player CLI")
    play_tvf_file(file_path, fps)

if __name__ == "__main__":
    main()
