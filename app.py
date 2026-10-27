"""Tiny sample application for the Coffee Corp workflow-file challenge."""

def brew_label(blend: str) -> str:
    """Return the label used for a prepared coffee batch."""

    return f"Coffee Corp batch: {blend}"

def main() -> None:
    print(brew_label("Workflow Blend"))


if __name__ == "__main__":
    main()
