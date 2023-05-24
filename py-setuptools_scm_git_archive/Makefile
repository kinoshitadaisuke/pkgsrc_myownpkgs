# $NetBSD$

DISTNAME=	setuptools_scm_git_archive-1.4
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/setuptools_scm_git_archive/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/Changaco/setuptools_scm_git_archive/
COMMENT=	setuptools_scm plugin for git archives
LICENSE=	mit

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

USE_LANGUAGES=	# none

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
