# $NetBSD$

DISTNAME=	gtts-2.5.4
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	python audio textproc
MASTER_SITES=	${MASTER_SITE_PYPI:=g/gtts/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/gtts/
COMMENT=	Python interface with Google Translate text-to-speech API
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=61:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-requests>=2.27:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-click>=7.1:../../devel/py-click

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
