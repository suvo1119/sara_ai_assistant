import { Button } from '@/components/ui/button';
import { cn } from '@/lib/utils';

interface WelcomeProps {
  disabled: boolean;
  startButtonText: string;
  onStartCall: () => void;
}

export const Welcome = ({
  disabled,
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeProps) => {
  return (
    <section
      ref={ref}
      inert={disabled}
      className={cn(
        'bg-background fixed inset-0 mx-auto flex h-svh flex-col items-center justify-center text-center',
        disabled ? 'z-10' : 'z-20'
      )}
    >
            <div className="relative inline-block">
        {/* Sara Avatar */}
        <img
          src="/sara.png"
          alt="Sara"
          className="w-[400px] h-auto rounded-full shadow-lg"
        />

        {/* Overlay content */}
        <div className="absolute bottom-6 left-1/2 transform -translate-x-1/2 text-center bg-black bg-opacity-70 px-6 py-4 rounded-lg inline-block">
  <Button
    variant="primary"
    size="lg"
    onClick={() => {
      // Play button click sound
      const clickSound = new Audio("/button-click.m4a");
      clickSound.volume = 0.3;
      clickSound.play();

      // Call your original function
      onStartCall();
    }}
    className="mt-4 w-100 font-mono"
  >
    {startButtonText}
  </Button>
</div>
      </div>
    </section>
  );
};
