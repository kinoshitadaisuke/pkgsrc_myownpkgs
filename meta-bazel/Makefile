# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-bazel-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs lang devel
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for bazel
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# pkgsrc_myownpkgs
DEPENDS+=	llvm>=0:../../pkgsrc_myownpkgs/llvm18
DEPENDS+=	clang>=0:../../pkgsrc_myownpkgs/clang18
DEPENDS+=	clang-tools-extra>=0:../../pkgsrc_myownpkgs/clang-tools-extra18
DEPENDS+=	bazel>=0:../../pkgsrc_myownpkgs/bazel

.include "../../mk/bsd.pkg.mk"
