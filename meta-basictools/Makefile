# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-basictools-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs shells graphics math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# security
DEPENDS+=	mozilla-rootcerts-openssl>=0:../../security/mozilla-rootcerts-openssl
DEPENDS+=	openssh>=0:../../security/openssh
DEPENDS+=	openssl>=0:../../security/openssl

# shells
DEPENDS+=	tcsh>=0:../../shells/tcsh
DEPENDS+=	zsh>=0:../../shells/zsh

# archivers
DEPENDS+=	bzip2>=0:../../archivers/bzip2
DEPENDS+=	bzip3>=0:../../archivers/bzip3
DEPENDS+=	gtar>=0:../../archivers/gtar
DEPENDS+=	unzip>=0:../../archivers/unzip
DEPENDS+=	xz>=0:../../archivers/xz
DEPENDS+=	zip>=0:../../archivers/zip

# audio
DEPENDS+=	open_jtalk>=0:../../audio/open_jtalk
DEPENDS+=	open_jtalk-HTS_voice>=0:../../audio/open_jtalk-HTS_voice
DEPENDS+=	open_jtalk-MMDAgent_voice>=0:../../audio/open_jtalk-MMDAgent_voice

# converters
DEPENDS+=	base64>=0:../../converters/base64
DEPENDS+=	dos2unix>=0:../../converters/dos2unix
#DEPENDS+=	unix2dos>=0:../../converters/unix2dos

# devel
DEPENDS+=	git>=0:../../devel/git
DEPENDS+=	php-mode>=0:../../devel/php-mode

# editors
DEPENDS+=	emacs29>=0:../../editors/emacs29
#DEPENDS+=	emacs30>=0:../../editors/emacs30
DEPENDS+=	vim>=0:../../editors/vim

# file systems
DEPENDS+=	fuse-exfat>=0:../../filesystems/fuse-exfat
DEPENDS+=	fuse-ext2>=0:../../filesystems/fuse-ext2

# lang
DEPENDS+=	gawk>=0:../../lang/gawk
DEPENDS+=	perl>=0:../../lang/perl5
DEPENDS+=	python39>=0:../../lang/python39
DEPENDS+=	python310>=0:../../lang/python310
DEPENDS+=	python311>=0:../../lang/python311
DEPENDS+=	python312>=0:../../lang/python312
DEPENDS+=	python313>=0:../../lang/python313
DEPENDS+=	tcl>=0:../../lang/tcl

# meta-pkgs
DEPENDS+=	pkg_developer>=0:../../meta-pkgs/pkg_developer

# misc
DEPENDS+=	lv>=0:../../misc/lv

# net
DEPENDS+=	openntpd>=0:../../net/openntpd
DEPENDS+=	openvpn>=0:../../net/openvpn
DEPENDS+=	rsync>=0:../../net/rsync
DEPENDS+=	tigervnc>=0:../../net/tigervnc
DEPENDS+=	wget>=0:../../net/wget
DEPENDS+=	wget2>=0:../../net/wget2
#DEPENDS+=	yt-dlp>=0:../../net/yt-dlp

# print
DEPENDS+=	ghostscript-agpl>=0:../../print/ghostscript-agpl
DEPENDS+=	gv>=0:../../print/gv
DEPENDS+=	okular>=0:../../print/okular
#DEPENDS+=	pdfjam>=0:../../print/pdfjam
DEPENDS+=	qpdf>=0:../../print/qpdf
DEPENDS+=	xpdf>=0:../../print/xpdf4

# sysutils
DEPENDS+=	coreutils>=0:../../sysutils/coreutils
DEPENDS+=	estd>=0:../../sysutils/estd
DEPENDS+=	gkrellm>=0:../../sysutils/gkrellm

# www
DEPENDS+=	curl>=0:../../www/curl

# pkgsrc_myownpkgs
DEPENDS+=	yatex>=0:../../pkgsrc_myownpkgs/yatex-mode
DEPENDS+=	yt-dlp>=0:../../pkgsrc_myownpkgs/yt-dlp

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
