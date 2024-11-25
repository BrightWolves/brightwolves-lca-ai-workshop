"""Environment setup helper for workshop notebooks.

This module helps set up the Python path for workshop notebooks to ensure
proper importing of team solution packages and access to workshop data.
"""
import os
import sys
from pathlib import Path
from typing import Optional, Dict, Any
import json


def find_repo_root(start_path: Optional[Path] = None) -> Path:
    """Find the repository root by looking for key directories.
    
    Args:
        start_path: Path to start searching from. Defaults to current directory.
    
    Returns:
        Path to repository root
        
    Raises:
        RuntimeError: If repository root cannot be found
    """
    if start_path is None:
        start_path = Path().absolute()
        
    current = start_path
    while current != current.parent:
        # Look for key directories that indicate repo root
        if all((current / d).exists() for d in ['exercises', 'solutions', 'data']):
            return current
        current = current.parent
        
    raise RuntimeError(
        f"Could not find repository root from {start_path}. "
        "Make sure you're running this from within the workshop repository."
    )


def verify_data_files() -> Dict[str, Path]:
    """Verify existence of required data files and return their paths.
    
    Returns:
        Dictionary mapping file descriptions to their paths
        
    Raises:
        FileNotFoundError: If required data files are missing
    """
    repo_root = find_repo_root()
    data_dir = repo_root / "data" / "reference_results"
    
    required_files = {
        'sample_epd': data_dir / 'sample_epd.pdf',
        'reference_calculations': data_dir / 'reference_calculations.csv',
        'validation_dataset': data_dir / 'validation_dataset.csv'
    }
    
    missing_files = [
        desc for desc, path in required_files.items() 
        if not path.exists()
    ]
    
    if missing_files:
        raise FileNotFoundError(
            f"Missing required data files: {', '.join(missing_files)}"
        )
        
    return required_files


def verify_team_solution(team_name: str = "team_template") -> None:
    """Verify team solution directory structure is correct.
    
    Args:
        team_name: Name of team directory to verify
        
    Raises:
        RuntimeError: If team directory structure is invalid
    """
    repo_root = find_repo_root()
    team_dir = repo_root / "solutions" / team_name
    
    required_dirs = [
        team_dir / "src",
        team_dir / "notebooks",
        team_dir / "tests",
        team_dir / "prompts"
    ]
    
    missing_dirs = [
        d for d in required_dirs 
        if not d.exists()
    ]
    
    if missing_dirs:
        raise RuntimeError(
            f"Invalid team directory structure. Missing: {', '.join(str(d) for d in missing_dirs)}"
        )


def setup_notebook_env() -> Dict[str, Any]:
    """Set up Python path and verify workshop environment.
    
    Returns:
        Dictionary containing environment information
        
    Raises:
        RuntimeError: If environment setup fails
    """
    try:
        # Find repo root
        repo_root = find_repo_root()
        
        # Add paths to Python path
        paths_to_add = [
            str(repo_root),
            str(repo_root / "solutions")
        ]
        
        for path in paths_to_add:
            if path not in sys.path:
                sys.path.append(path)
                
        # Verify environment
        data_files = verify_data_files()
        verify_team_solution()
        
        # Try imports
        import team_template.src.extraction
        import team_template.src.processing
        
        env_info = {
            'repo_root': repo_root,
            'data_files': data_files,
            'python_paths': paths_to_add
        }
        
        print("Environment setup complete! ✨")
        print("\nPython path additions:")
        for path in paths_to_add:
            print(f"  - {path}")
        print("\nVerified data files:")
        for desc, path in data_files.items():
            print(f"  - {desc}: {path}")
            
        return env_info
        
    except Exception as e:
        print(f"❌ Environment setup failed: {str(e)}")
        print("\nPlease make sure:")
        print("1. You're running this notebook from within the workshop repository")
        print("2. All required data files are present")
        print("3. Your team solution directory is properly structured")
        raise


if __name__ == "__main__":
    setup_notebook_env()