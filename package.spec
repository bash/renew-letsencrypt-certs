Name: certbot-wrapper
Version: 0.1.0
Release: 1%{?dist}
Summary: A wrapper around certbot with some extras ✨
License: MIT

BuildRequires: rust-packaging
VCS: {{{ git_dir_vcs }}}
Source: {{{ git_dir_pack }}}

%description
%{summary}.

%prep
{{{ git_dir_setup_macro }}}

%changelog
{{{ git_dir_changelog }}}
