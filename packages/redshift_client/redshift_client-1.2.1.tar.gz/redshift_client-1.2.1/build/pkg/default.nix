{
  lib,
  metadata,
  nixpkgs,
  python_pkgs,
  src,
}: let
  runtime_deps = with python_pkgs; [
    psycopg2
    types-psycopg2
    fa-purity
  ];
  build_deps = with python_pkgs; [flit-core];
  test_deps = with python_pkgs; [
    import-linter
    mypy
    pytest
  ];
  pkg = (import ./build.nix) {
    inherit lib src metadata runtime_deps build_deps test_deps;
  };
  build_env = extraLibs:
    lib.buildEnv {
      inherit extraLibs;
      ignoreCollisions = false;
    };
  _dev_env = build_env (runtime_deps ++ test_deps ++ build_deps);
  dev_env = nixpkgs.mkShell {
    dev_env = _dev_env;
    auto_conf = ./vs_settings.py;
    conf_python = nixpkgs.python310;
    packages = [_dev_env];
    shellHook = ./dev_env_hook.sh;
  };
in {
  inherit pkg;
  env.runtime = build_env runtime_deps;
  env.dev = dev_env;
  env.bin = build_env [pkg];
}
