import { useState } from "react";
import { Loader2, Copy, Check, Terminal, Sparkles } from "lucide-react";
import { useToast } from "@/hooks/use-toast";

const Index = () => {
  const [instruction, setInstruction] = useState("");
  const [generatedCode, setGeneratedCode] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [copied, setCopied] = useState(false);
  const { toast } = useToast();

  const handleGenerate = async () => {
    if (!instruction.trim()) {
      toast({
        title: "Empty instruction",
        description: "Please enter an instruction to generate code.",
        variant: "destructive",
      });
      return;
    }

    setIsLoading(true);
    setError(null);
    setGeneratedCode("");

    try {
      const response = await fetch("http://127.0.0.1:8000/generate", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ instruction: instruction.trim() }),
      });

      if (!response.ok) {
        throw new Error(`Request failed with status ${response.status}`);
      }

      const data = await response.json();
      setGeneratedCode(data.code || "// No code generated");
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : "An unknown error occurred";
      setError(errorMessage);
      toast({
        title: "Generation failed",
        description: errorMessage,
        variant: "destructive",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleCopy = async () => {
    if (!generatedCode) return;
    
    try {
      await navigator.clipboard.writeText(generatedCode);
      setCopied(true);
      toast({
        title: "Copied!",
        description: "Code copied to clipboard.",
      });
      setTimeout(() => setCopied(false), 2000);
    } catch {
      toast({
        title: "Copy failed",
        description: "Failed to copy code to clipboard.",
        variant: "destructive",
      });
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) {
      handleGenerate();
    }
  };

  return (
    <div className="min-h-screen bg-background p-4 md:p-8">
      <div className="mx-auto max-w-4xl">
        {/* Header */}
        <header className="mb-8 text-center">
          <div className="mb-2 inline-flex items-center gap-2 rounded-full bg-secondary px-4 py-1.5 text-sm text-muted-foreground">
            <Terminal className="h-4 w-4" />
            <span>AI Code Generator</span>
          </div>
          <h1 className="text-3xl font-semibold tracking-tight text-foreground md:text-4xl">
            Generate code with AI
          </h1>
          <p className="mt-2 text-muted-foreground">
            Describe what you want to build and get code instantly.
          </p>
        </header>

        {/* Input Section */}
        <div className="mb-6">
          <label htmlFor="instruction" className="mb-2 block text-sm font-medium text-foreground">
            Your instruction
          </label>
          <textarea
            id="instruction"
            value={instruction}
            onChange={(e) => setInstruction(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Describe the code you want to generate..."
            className="input-glow min-h-[140px] w-full resize-none rounded-lg border border-border bg-input px-4 py-3 font-mono text-sm text-foreground placeholder:text-muted-foreground focus:border-ring focus:outline-none"
            disabled={isLoading}
          />
          <p className="mt-1.5 text-xs text-muted-foreground">
            Press <kbd className="rounded bg-secondary px-1.5 py-0.5 font-mono">⌘</kbd> + <kbd className="rounded bg-secondary px-1.5 py-0.5 font-mono">Enter</kbd> to generate
          </p>
        </div>

        {/* Generate Button */}
        <button
          onClick={handleGenerate}
          disabled={isLoading || !instruction.trim()}
          className="glow-button mb-8 flex w-full items-center justify-center gap-2 rounded-lg bg-primary px-6 py-3 font-medium text-primary-foreground transition-colors hover:bg-primary/90 disabled:cursor-not-allowed disabled:opacity-50"
        >
          {isLoading ? (
            <>
              <Loader2 className="h-5 w-5 animate-spin" />
              <span>Generating...</span>
            </>
          ) : (
            <>
              <Sparkles className="h-5 w-5" />
              <span>Generate Code</span>
            </>
          )}
        </button>

        {/* Output Section */}
        <div className="code-panel">
          <div className="code-header">
            <div className="flex items-center gap-2">
              <div className="flex gap-1.5">
                <span className="h-3 w-3 rounded-full bg-destructive/60" />
                <span className="h-3 w-3 rounded-full bg-yellow-500/60" />
                <span className="h-3 w-3 rounded-full bg-green-500/60" />
              </div>
              <span className="ml-2">output</span>
            </div>
            {generatedCode && (
              <button
                onClick={handleCopy}
                className="flex items-center gap-1.5 rounded px-2 py-1 text-xs transition-colors hover:bg-secondary hover:text-foreground"
              >
                {copied ? (
                  <>
                    <Check className="h-3.5 w-3.5" />
                    <span>Copied</span>
                  </>
                ) : (
                  <>
                    <Copy className="h-3.5 w-3.5" />
                    <span>Copy</span>
                  </>
                )}
              </button>
            )}
          </div>
          <div className="code-content text-foreground">
            {isLoading ? (
              <div className="flex items-center gap-2 text-muted-foreground">
                <Loader2 className="h-4 w-4 animate-spin" />
                <span>Generating your code...</span>
              </div>
            ) : error ? (
              <div className="text-destructive">
                <span className="font-semibold">Error:</span> {error}
              </div>
            ) : generatedCode ? (
              generatedCode
            ) : (
              <span className="text-muted-foreground">
                Generated code will appear here...
              </span>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
