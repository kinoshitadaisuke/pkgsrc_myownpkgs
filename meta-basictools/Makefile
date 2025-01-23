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

# converters
DEPENDS+=	base64>=0:../../converters/base64
DEPENDS+=	dos2unix>=0:../../converters/dos2unix
#DEPENDS+=	unix2dos>=0:../../converters/unix2dos

# devel
DEPENDS+=	php-mode>=0:../../devel/php-mode

# editors
DEPENDS+=	emacs29>=0:../../editors/emacs29

# file systems
DEPENDS+=	fuse-exfat>=0:../../filesystems/fuse-exfat
DEPENDS+=	fuse-ext2>=0:../../filesystems/fuse-ext2

# graphics
DEPENDS+=	adwaita-icon-theme>=0:../../graphics/adwaita-icon-theme

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
DEPENDS+=	yt-dlp>=0:../../net/yt-dlp

# print
DEPENDS+=	gv>=0:../../print/gv
DEPENDS+=	okular>=0:../../print/okular
DEPENDS+=	pdfjam>=0:../../print/pdfjam
DEPENDS+=	qpdf>=0:../../print/qpdf
DEPENDS+=	xpdf>=0:../../print/xpdf4

# sysutils
DEPENDS+=	estd>=0:../../sysutils/estd
DEPENDS+=	gkrellm>=0:../../sysutils/gkrellm

# time
DEPENDS+=	emiclock>=0:../../time/emiclock
DEPENDS+=	oclock>=0:../../time/oclock
DEPENDS+=	xclock>=0:../../time/xclock

# wm
DEPENDS+=	fvwm3>=0:../../wm/fvwm3

# www
DEPENDS+=	curl>=0:../../www/curl

# x11
DEPENDS+=	kde-workspace4>=0:../../x11/kde-workspace4
DEPENDS+=	kterm>=0:../../x11/kterm
DEPENDS+=	xcursor-capitaine>=0:../../x11/xcursor-capitaine
DEPENDS+=	xcursor-core-hr>=0:../../x11/xcursor-core-hr
DEPENDS+=	xcursor-themes>=0:../../x11/xcursor-themes
DEPENDS+=	xcursor-vanilla-dmz>=0:../../x11/xcursor-vanilla-dmz
DEPENDS+=	xdotool>=0:../../x11/xdotool
DEPENDS+=	xterm>=0:../../x11/xterm

# pkgsrc_myownpkgs
DEPENDS+=	yatex>=0:../../pkgsrc_myownpkgs/yatex-mode

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
